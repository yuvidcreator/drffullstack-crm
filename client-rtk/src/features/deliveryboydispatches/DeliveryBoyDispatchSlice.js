import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import DeliveryBoyDispatchAPIService from './DeliveryboyDispatchAPIService';


const user = JSON.parse(localStorage.getItem("user"));

const initialState = {
    user: user ? user : null,
    deliveryboydispatchelists: [],
    deliveryboydispatchset: {},
    isError: false,
    isLoading: false,
    isSuccess: false,
    message: ''
};


// get all Delivery Boy's disptach list
export const getDeliveryBoyDispatchList = createAsyncThunk(
    "deliveryboydispatches/getAll", 
    async (user, thunkAPI) => {
        try {
            return await DeliveryBoyDispatchAPIService.getDeliveryBoyDispatchList(user);
        } catch (error) {
            const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
);



export const DeliveryBoyDispatchSlice = createSlice({
    name: 'deliveryboydispatch',
    initialState,
    reducers: {
        reset: (state) => initialState
    },
    extraReducers: (builder) => {
        builder
            .addCase(getDeliveryBoyDispatchList.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(getDeliveryBoyDispatchList.fulfilled, (state, action) => {
                state.isLoading = false;
                state.isSuccess = true;
                state.mydispatchelists = action.payload.dispatchdata;
            })
            .addCase(getDeliveryBoyDispatchList.rejected, (state, action) => {
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
            });
    },
});

export const {reset} = DeliveryBoyDispatchSlice.actions;
export default DeliveryBoyDispatchSlice.reducer;
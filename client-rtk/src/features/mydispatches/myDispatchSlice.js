import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import myDispatchAPIService from './myDispatchAPIService';



const initialState = {
    mydispatchelists: [],
    mydispatchset: {},
    isError: false,
    isLoading: false,
    isSuccess: false,
    message: ''
};


// get all my disptach list
export const getMyDispatches = createAsyncThunk(
    "mydispatches/getAll", 
    async (_, thunkAPI) => {
        try {
            return await myDispatchAPIService.getMyDispatches();
        } catch (error) {
            const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
);


export const myDispatchSlice = createSlice({
    name: 'mydispatch',
    initialState,
    reducers: {
        reset: (state) => initialState
    },
    extraReducers: (builder) => {
        builder
            .addCase(getMyDispatches.pending, (state) => {
                state.isLoading = true;
            })
            .addCase(getMyDispatches.fulfilled, (state, action) => {
                state.isLoading = false;
                state.isSuccess = true;
                state.mydispatchelists = action.payload.dispatchdata;
            })
            .addCase(getMyDispatches.rejected, (state, action) => {
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
            });
    },
});

export const {reset} = myDispatchSlice.actions;
export default myDispatchSlice.reducer;
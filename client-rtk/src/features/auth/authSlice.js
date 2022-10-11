import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import authAPIService from './authAPIService';


const userToken = JSON.parse(localStorage.getItem("userToken"));
const user = JSON.parse(localStorage.getItem("user"));

const initialState = {
    userToken: userToken ? userToken : null,
    user: user ? user: null,
    isError: false,
    isLoading: false,
    isSuccess: false,
    message: ''
};


export const register = createAsyncThunk(
    "auth/register",
    async(userData, thunkAPI) => {
        try {
            return await authAPIService.register(userData);
        } catch (error) {
            const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
);


export const login = createAsyncThunk(
    "auth/login",
    async(userData, thunkAPI) => {
        try {
            return await authAPIService.login(userData);
        } catch (error) {
            const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
);


export const logout = createAsyncThunk(
    "auth/logout",
    async() => {
        authAPIService.logout();
    }
);


export const activate = createAsyncThunk(
    "auth/activate",
    async(userData, thunkAPI) => {
        try {
            return authAPIService.activate(userData);
        } catch (error) {
            const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString();
            return thunkAPI.rejectWithValue(message);
        }
    }
)


export const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        reset: (state) => {
            state.isLoading = false;
            state.isError = false;
            state.isSuccess = false;
            state.message = '';
        },
    },

    extraReducers: (builder) => {
        builder
            .addCase(register.pending, (state)=>{
                state.isLoading = true;
            })
            .addCase(register.fulfilled, (state, action)=>{
                state.isLoading = false;
                state.isSuccess = true;
                state.userToken = action.payload;
                state.user = action.payload;
            })
            .addCase(register.rejected, (state, action)=>{
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.userToken = null;
                state.user = null;
            })
            .addCase(login.pending, (state)=>{
                state.isLoading = true;
            })
            .addCase(login.fulfilled, (state, action)=>{
                state.isLoading = false;
                state.isSuccess = true;
                state.userToken = action.payload;
                state.user = action.payload;
            })
            .addCase(login.rejected, (state, action)=>{
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.userToken = null;
                state.user = null;
            })
            .addCase(logout.fulfilled, (state)=>{
                state.userToken = null;
                // state.user = null;
            })
            .addCase(activate.pending, (state)=>{
                state.isLoading = true;
            })
            .addCase(activate.fulfilled, (state, action)=>{
                state.isLoading = false;
                state.isSuccess = true;
            })
            .addCase(activate.rejected, (state, action)=>{
                state.isLoading = false;
                state.isError = true;
                state.message = action.payload;
                state.userToken = null;
                state.user = null;
            });
    }
});


export const {reset} = authSlice.actions;

export default authSlice.reducer;
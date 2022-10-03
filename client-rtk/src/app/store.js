import { configureStore } from '@reduxjs/toolkit';
import myDispatchReducer from '../features/mydispatches/myDispatchSlice';
import authReducer from '../features/auth/authSlice';

export const store = configureStore({
  reducer: {
    myDispatches: myDispatchReducer,
    auth: authReducer,
  },
});

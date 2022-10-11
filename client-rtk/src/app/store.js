import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import myDispatchReducer from '../features/mydispatches/myDispatchSlice';
import DeliveryBoyDispatchReducer from '../features/deliveryboydispatches/DeliveryBoyDispatchSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    myDispatches: myDispatchReducer,
    DeliveryBoyDispatches: DeliveryBoyDispatchReducer,
  },
});

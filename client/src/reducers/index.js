import { combineReducers } from 'redux';
import { myDispatchReducers } from './myDispatchReducers';

export default combineReducers({
    myDispatchList: myDispatchReducers,
});
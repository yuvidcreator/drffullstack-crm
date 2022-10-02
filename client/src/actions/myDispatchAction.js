import axios from 'axios';
import {API_URL} from '../config/apiEndPoint'
import {
    MYDISPATCH_LIST_REQUEST,
    MYDISPATCH_LIST_SUCCESS,
    MYDISPATCH_LIST_FAIL
} from './types'



export const listMyDispatch = () => async (dispatch) => {
    try {
        dispatch({
            type: MYDISPATCH_LIST_REQUEST,
        });

        const {data} = await axios.get(`${API_URL}/api/v1/dispatch/all/`);

        dispatch({
            type: MYDISPATCH_LIST_SUCCESS,
            payload: data
        });

    } catch(error) {
        dispatch({
            type: MYDISPATCH_LIST_FAIL,
            payload: 
                error.response && error.response.data.message 
                    ? error.response.data.message 
                    : error.message,
        });
    }
}
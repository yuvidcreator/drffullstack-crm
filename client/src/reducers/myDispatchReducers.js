import {
    MYDISPATCH_LIST_REQUEST,
    MYDISPATCH_LIST_SUCCESS,
    MYDISPATCH_LIST_FAIL
} from '../actions/types'


export const myDispatchReducers = (
        state = { mydispatch: [] }, action
    ) => {
        switch (action.type) {

            case MYDISPATCH_LIST_REQUEST:
                return {loading: true, mydispatch:[]}

            case MYDISPATCH_LIST_SUCCESS:
                return {loading: false, mydispatch:action.payload}

            case MYDISPATCH_LIST_FAIL:
                return {loading:false, error: action.payload}

            default:
                return state;
        }
    };
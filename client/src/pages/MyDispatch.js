import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { listMyDispatch } from '../actions/myDispatchAction';


const MyDispatch = () => {
    const dispatch = useDispatch();

    const myAllDispatchLists = useSelector((state) => state.myDispatchList);

    const { loading, error, mydispatch } = myAllDispatchLists;

    useEffect(() => {
        dispatch(listMyDispatch());
    }, [dispatch])

    console.log(mydispatch);

    return (
        <>
            <div>
                {loading ? (
                    <div>
                        {/* spinner */}
                    </div>
                    ) : error ? (
                        // alert
                        <div>
                            {error.message}
                        </div>
                    ) : (
                        <div>
                            {mydispatch.map((property)=>(
                                <div key={property.id}>
                                    <h3>{property.party_name}</h3>
                                </div>
                            ))}
                        </div>
                    )
                }
            </div>
        </>
    )
}

export default MyDispatch
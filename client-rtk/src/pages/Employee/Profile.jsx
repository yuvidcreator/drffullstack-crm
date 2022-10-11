import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Container } from 'react-bootstrap';
import Spinner from '../../components/Spinner';
import {toast} from 'react-toastify';


const Profile = () => {

    const dispatch = useDispatch();

    const { user, isLoading, isError, message } = useSelector((state) => state.auth);

    // const apiDataGet = useSelector((state) => state.auth.getUserInfo);

    // console.log(apiDataGet);
    // console.log(user.employee);

    const userData = user.employee;

    // console.log(userData);

    useEffect(() => {
        if (isError) {
            toast.error(message, {icon: "😜"});
        }
        // dispatch(getUserInfo());

    }, [dispatch, user, isError, message]);

    if (isLoading) {
        <Spinner />;
    }

    return (
        <div className="mt-5 mt-lg-5 mt-md-5">
            <Container className="d-flex h-100 align-items-center justify-content-center text-center">
                <div className="d-flex justify-content-center mt-5 mt-lg-5 mt-md-5">
                    <div className="text-center mt-lg-5 mt-md-5 mt-5">
                        
                        <h2 className="mx-auto mb-5">
                            Employee Profile
                        </h2>
                        <p>{userData.country}</p>
                    </div>
                </div>
            </Container>
        </div>
    )
}

export default Profile
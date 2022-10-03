import React, {useState, useEffect} from 'react';
import {Container, Form, Button, Row, Col} from 'react-bootstrap';
import { MdLogin } from 'react-icons/md';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import Spinner from '../components/Spinner';
import { login, reset } from '../features/auth/authSlice';


const LoginPage = () => {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const {user, isError, isLoading, isSuccess, message} = useSelector((state) => state.auth);

    useEffect(() => {
        if (isError) {
            toast.error(message);
        }

        if (isSuccess || user ) {
            navigate("/employee");
        }

        dispatch(reset());
    }, [isError, isSuccess, message, user, navigate, dispatch]);

    const submitHandler = (e) => {
        e.preventDefault();

        if (!email) {
            toast.error("An Email must be provided");
        }

        if (!password) {
            toast.error("An Password must be provided");
        }

        const userData = {
            email, password
        };

        dispatch(login(userData));
    }

    return (
        <>
            <Container className="d-flex">
                <Container>
                    <Row>
                        <Col className="mg-top text-center">
                            <section>
                                <h1>
                                    <MdLogin /> Login
                                </h1>
                                <hr className="hr-text" />
                            </section>
                        </Col>
                    </Row>

                    {isLoading && <Spinner />}

                    <Row className="mt-3">
                        <Col className="justify-content-center">
                            <Form onSubmit={submitHandler}>
                                <Form.Group controlId="email" className="mt-3">
                                    <Form.Label>Email ID</Form.Label>
                                    <Form.Control 
                                        type="email" 
                                        placeholder="Enter Email ID" 
                                        value={email} 
                                        onChange={(e)=>setEmail(e.target.value)} 
                                    />
                                </Form.Group>
                                <Form.Group controlId="password" className="mt-3">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Control
                                        type="password" 
                                        placeholder="Enter Password" 
                                        value={password} 
                                        onChange={(e)=>setPassword(e.target.value)} 
                                    />
                                </Form.Group>
                                <Button type="submit" variant="primary" className="mt-3">
                                    Sign In
                                </Button>
                            </Form>
                        </Col>
                    </Row>

                    <Row className="py-4">
                        <Col>
                            New Employee?
                            <Link to="/signup" className="mx-2">Register Here....</Link>
                        </Col>
                    </Row>

                    <Row>
                        <Col>
                            Forget Password?
                            <Link to="/resetpass" className="mx-2">Reset Password</Link>
                        </Col>
                    </Row>
                </Container>
            </Container>
        </>
    )
};

export default LoginPage;
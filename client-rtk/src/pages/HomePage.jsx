import React from 'react';
import { Container, Button } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';


const HomePage = () => {
    return (
        <div className="masthead main-bg-image mt-12">
            <Container className="d-flex h-100 align-items-center justify-content-center text-center">
                <div className="d-flex justify-content-center">
                    <div className="text-center">
                        <h1 className="mx-auto my-0 text-uppercase">
                            Yantrayug Hero Hub
                        </h1>
                        <h2 className="text-white-50 mx-auto mt-2 mb-5">
                            The Best Auto Parts store in Pune.
                            The Yantrayug Herohub.
                        </h2>
                        <LinkContainer to="/dispatch">
                            <Button variant="primary">Get Live Update</Button>
                        </LinkContainer>
                    </div>
                </div>
            </Container>
        </div>
    )
}

export default HomePage
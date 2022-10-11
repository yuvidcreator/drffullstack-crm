import React from 'react';
import { Container, Button } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';


const HomePage = () => {
    return (
        <div className="mt-5 mt-lg-5 mt-md-5">
            <Container className="d-flex h-100 align-items-center justify-content-center text-center">
                <div className="d-flex justify-content-center mt-5 mt-lg-5 mt-md-5">
                    <div className="text-center mt-lg-5 mt-md-5 mt-5">
                        
                        <h2 className="mx-auto mb-5">
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
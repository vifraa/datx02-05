import React, { Component } from 'react'
import {
    MDBBtn,
    MDBCard,
    MDBCardBody,
    MDBCardImage,
    MDBCardTitle,
    MDBIcon,
  } from "mdbreact";
  import { Row, Container } from "react-bootstrap";

  
export default class generatedFileCard extends Component {
    render() {
        return (
            <div>
                <Container>
                    <Row>
                        <MDBCard
                            className="h-100"
                            cascade
                        >
                            <MDBCardImage
                                cascade
                                className="img-fluid"
                                overlay="white-light"
                                hover
                                height="400 px"
                                width="400 px"
                                src={"https://lh3.googleusercontent.com/proxy/x5h9k-MEkp9bqNgYw49pu7GfCIabeisfD5z7y76JqmSZnc_ye3Sw5obrzVY_aNtEK9yHxjJOBHSiQDc5bEAt0rghzD2KGoGIinnYIsAZAM6vUgYOHllBZ1HD_Z97N2KijX-oMEvT7DaX26DeMRQt3WGc-bN54nzm8mo"}
                            />
                            <MDBBtn
                                floating
                                tag="a"
                                className="ml-auto lighten-3 mdb-coalor"
                                action
                            >
                                <MDBIcon icon="chevron-right" className="mdb-color lighten-3" />
                            </MDBBtn>
                            <MDBCardBody cascade>
                                <MDBCardTitle id="cardTitle">
                                    {this.props.csvName}
                                </MDBCardTitle>
                                <MDBCardText>
                                    {this.props.csvshape}
                                </MDBCardText>
                            </MDBCardBody>
                        </MDBCard>
                    </Row>
                </Container>

            </div>
        )
    }
}

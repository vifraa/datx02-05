import React, { Component } from 'react';

class modelCard extends Component {
    render() {
        return (
            <div>
                <MDBRow className="justify-content-center">
                    <MDBCol md="4">
                        <MDBCard cascade onClick={() => { window.location.replace('/Lift'); }}>
                            <MDBCardImage
                                cascade
                                className='img-fluid'
                                overlay="white-light"
                                hover
                                src='https://wwwcibesliftcom.cdn.triggerfish.cloud/uploads/2018/07/cabinliftcibesa6000.png'
                            />
                            <MDBBtn
                                floating
                                tag='a'
                                className='ml-auto mr-4 lighten-3 mdb-coalor'
                                action
                            >
                                <MDBIcon icon='chevron-right' className="mdb-color lighten-3" />
                            </MDBBtn>
                            <MDBCardBody cascade>
                                <MDBCardTitle>Lift</MDBCardTitle>
                                <hr />
                            </MDBCardBody>
                        </MDBCard>
                    </MDBCol>     
                </MDBRow>
            </div>
                );
            }
        }
        
export default modelCard;
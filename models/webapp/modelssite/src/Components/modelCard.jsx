import React, { Component } from 'react';

class modelCard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            regression_results:""
        }
    }

    run_regression(ModelName){
        fetch("http://127.0.0.1:5000/models/regression/" + ModelName)
        .then(res => res.text())
        .then((data) => {
            this.setState({regression_results : data});
            this.write_text("regression_output", data);
        }).catch(console.log);
    }

    write_text(element_id, txt){
        console.log(txt);
        document.getElementById(element_id).innerHTML=txt;
    }
    
    render() {
        return (
            <div>
                <MDBRow className="justify-content-center">
                    <MDBCol md="4">
                        <MDBCard cascade onClick={()=>{this.run_regression('this.props.model_name')}}>
                            <MDBCardImage
                                cascade
                                className='img-fluid'
                                overlay="white-light"
                                hover
                                src={this.props.model_img}
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
                                <MDBCardTitle>{this.props.model_name}</MDBCardTitle>
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
import React, { Component } from 'react';
import { MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBRow, MDBCol, MDBIcon } from 'mdbreact';

class modelCard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            regression_results: ""
        }
    }

    run_regression(ModelName) {
        fetch("http://127.0.0.1:5000/models/regression/" + ModelName)
            .then(res => res.text())
            .then((data) => {
                this.setState({ regression_results: data });
                this.write_text("regression_output", data);
            }).catch(console.log);
    }

    write_text(element_id, txt) {
        console.log(txt);
        document.getElementById(element_id).innerHTML = txt;
    }

    render() {
        return (
            <div className="p-2 flex-fill bd-highlight col-example">
                <MDBCard className="h-100" cascade onClick={() => { this.run_regression(this.props.model_run_name) }}>
                    <MDBCardImage
                        cascade
                        className='img-fluid'
                        overlay="white-light"
                        hover
                        height="400 px"
                        width="400 px"
                        src={this.props.model_img}
                    />
                    <MDBBtn
                        floating
                        tag='a'
                        className='ml-auto lighten-3 mdb-coalor'
                        action
                    >
                        <MDBIcon icon='chevron-right' className="mdb-color lighten-3" />
                    </MDBBtn>
                    <MDBCardBody cascade>
                        <MDBCardTitle id="cardTitle">{this.props.model_name}</MDBCardTitle>
                    </MDBCardBody>
                </MDBCard>
            </div>
        );
    }
}

export default modelCard;
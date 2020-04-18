import React, { Component } from "react";
import {
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBCardTitle,
  MDBIcon,
} from "mdbreact";

import { Row, Container } from "react-bootstrap";


class modelCard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      regression_results: "",
      img_url: "",
    };
  }


  run_regression_and_curves(ModelName) {
    fetch("http://127.0.0.1:5000/models/regression/" + ModelName)
      .then((res) => res.text())
      .then((data) => {
        this.setState({ regression_results: data });
        fetch("http://127.0.0.1:5000/models/plot/" + ModelName)
        .then((ires) => ires.blob())
        .then((images) => {
            const objectURL = URL.createObjectURL(images);
            console.log("Learning curve URL: " + objectURL);
            this.setState({ img_url: objectURL });
            this.write_text_and_show_plot("regression_output", data, "learning_curves_output", objectURL);
        });
      })
      .catch(console.log);
  }

  write_text_and_show_plot(text_element_id, txt, img_element_id, objectURL) {
    console.log(txt);
    document.getElementById(text_element_id).innerHTML = txt;
    document.getElementById(img_element_id).src = objectURL;
}

  render() {      
        
    return (
          <MDBCard
            className="h-110 mr-3"
            cascade
            onClick={() => {
              this.run_regression_and_curves(this.props.model_run_name);
            }}
          >
            <MDBCardImage
              cascade
              className="img-fluid"
              overlay="white-light"
              hover
              height="400px"
              width="400px"
              src={this.props.model_img}
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
                {this.props.model_name}
              </MDBCardTitle>
            </MDBCardBody>
          </MDBCard>
    );
  }
}

export default modelCard;

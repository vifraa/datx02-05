import React, { Component } from "react";
import {
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBCardTitle,
  MDBRow,
  MDBCol,
  MDBIcon,
} from "mdbreact";

class learningResults extends Component {
  constructor(props) {
      super(props);
    this.state = {
      img_url: "",
    };
  }

   runLearningCurves(ModelName) {
    fetch("http://127.0.0.1:5000/models/plot/" + ModelName)
      .then((res) => res.blob())
      .then((images) => {
        const objectURL = URL.createObjectURL(images);
        console.log("Learning curve URL: " + objectURL);
       this.setState({ img_url: objectURL });
      });
  }

  render() {
    return (
      <div>
        <pre className="h-100" id="regression_output">
          Click on a model and you will see the results of the regression here..
        </pre>
        <img src={this.state.img_url}></img>
      </div>
    );
  }}

export default learningResults;

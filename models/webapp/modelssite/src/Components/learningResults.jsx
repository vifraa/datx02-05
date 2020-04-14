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
    };
  
  render() {
    return (
      <div>
        <pre className="h-10" id="regression_output">
          Click on a model and you will see the results of the regression here..
        </pre>
        <div>
            <img id="learning_curves_output" src="" className="visible margin-auto" alt="learning curves" height="100%" width="100%"></img>
        </div>
      </div>
    );
  }}

export default learningResults;


/**
 *         
 */
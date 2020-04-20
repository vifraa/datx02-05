import React, { Component } from "react";

class learningResults extends Component {

  render() {
    return (
      <div>
        <h3>Learning Results:</h3>
        <pre className="information_section" id="regression_output">
          Click on a model and you will see the results of the regression here..
        </pre>
        <div>
            <h3>Learning Curves:</h3>
            <img id="learning_curves_output" src="" className="visible margin-auto information_section" alt="learning curves" height="100%" width="100%"></img>
        </div>
      </div>
    );
  }}

export default learningResults;


/**
 *         
 */
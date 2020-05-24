import React, { Component } from "react";

class learningResults extends Component {

  render() {
    return (
      <div>
        <div className="rcorners">
          <h5>Learning Results:</h5>
          <pre id="regression_output">
          </pre>
        </div>

        <div className="rcorners">
            <h5>Learning Curves:</h5>
            <img id="learning_curves_output" src="" className="invisible margin-auto information_section" alt="learning curves" height="100%" width="100%"></img>
        </div>
      </div>
    );
  }}

export default learningResults;


/**
 *         
 */
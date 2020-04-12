import React, { Component } from "react";
import ModelsContainer from "./modelCardsContainer";
import UploadData from "./uploadData.jsx";

class main extends Component {
  render() {
    return (
      <div>
        Hello World!
        <UploadData />
        <ModelsContainer />
        <input
          type="file"
          name="file"
          onChange={
            (this.onChangeHandler = (event) => {
              console.log(event.target.files[0]);
            })
          }
        />
      </div>
    );
  }
}

export default main;

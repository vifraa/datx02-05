import React, { Component } from "react";
import "../../CSS_Folder/uploadData.css"; 

class uploadData extends Component {
  render() {
    return (
      <div className="container pt-3 flex">
        <div className="row">
          <div className="col-md-4">
            <form method="post" action="#" id="#">
              <div className="form-group files">
                <input type="file" className="form-control" multiple="" />
              </div>
            </form>
          </div>
          <div className="col-md-4 m-auto">
            <label>You can choose to upload your csv file here or to run on the default simulated individuals medium data set </label>
          </div>

        </div>
      </div>
    );  
  }
}

export default uploadData;

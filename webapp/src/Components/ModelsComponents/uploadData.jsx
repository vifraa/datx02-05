import React, { Component } from "react";
import "../../CSS_Folder/uploadData.css";

class uploadData extends Component {
  render() {
    return (
      <div className="container pt-3 flex">
        <div className="row">
          <div className="col-md-4">
           
            <form action="http://mo-yazanghafir.pagekite.me/simulator/upload" method="post" enctype="multipart/form-data">
              <input type="file" name="fileupload" id="fileToUpload"></input>
              <input type="submit" value="Upload File" name="submit"></input>
            </form>

          </div>
            <div className="col-md-4 m-auto">
              <label>You can choose to upload your trainingdata csv file here</label>
            </div>

          </div>
        </div>
        );  
      }
    }
    
    export default uploadData;

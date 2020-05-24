import React, { Component } from "react";
import "../../CSS_Folder/uploadData.css";

class uploadData extends Component {
  render() {
    return (
      <div className="rcorners" id="upload_data_container">
            <h5>Manually upload a data set:</h5>
            <form action="http://mo-yazanghafir.pagekite.me/simulator/upload" method="post" enctype="multipart/form-data">
              <input type="file" name="fileupload" id="fileToUpload" ></input>
              <input type="submit" value="Upload File" name="submit"></input>
            </form>
        </div>
        );  
      }
    }
    
    export default uploadData;


    
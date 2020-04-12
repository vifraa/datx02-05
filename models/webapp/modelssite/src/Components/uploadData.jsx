import React, { Component } from "react";
import "../CSS_Folder/uploadData.css"; 
import { userEndpoint } from "../endpoints";

async function getUserList(){
    try{
       const result = await userEndpoint.get(); 
       return console.log("RESPONSE: " + JSON.stringify(result.data));
    } catch (e) {
       console.log("That didnt go well");
    }
 }
class uploadData extends Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <form method="post" action="#" id="#">
              <div className="form-group files">
                <label>Upload Your File </label>
                <input type="file" className="form-control" multiple="" />
              </div>
            </form>
            <button onClick={() => getUserList()}>CLICK ME AND INSPECT</button>
          </div>
        </div>
      </div>
    );  
  }
}

export default uploadData;

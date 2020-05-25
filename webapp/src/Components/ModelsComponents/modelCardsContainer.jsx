import React, { Component } from "react";
import ModelCard from "./modelCard";
import LearningResults from "./learningResults";
import GeneratedFilesInfo from "../SimulatorComponents/generatedfilesInfo";
import Select from 'react-select'
import ModelUse from './modelUse';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import UploadData from './uploadData';

export default class modelCardsContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      model_names_and_images: [],
      datasetOptions: [],
      selectedDataset: ""
    };
    this.handleDropdownChange=this.handleDropdownChange.bind(this);
  }

  componentDidMount() {
    fetch("http://si-yazanghafir.pagekite.me/models")
      .then((res) => res.json())
      .then((data) => {
        this.setState({ model_names_and_images: data });
      })
      .catch(console.log);
      this.datasetOptions();
  }

  datasetOptions() {
        fetch("http://mo-yazanghafir.pagekite.me/simulator/trainingsets")
            .then(res => res.json())
            .then((data) => {
                let options = [];
                data.forEach(name => {
                    let option = {value: name[0], label: name[0]};
                    options.push(option);
                });
                this.setState({ datasetOptions: options });
                console.log(this.options);
            }).catch(console.log);
  }
  handleDropdownChange(e){
      this.setState({selectedDataset: e.value});
  }



  compare(){
      fetch("http://si-yazanghafir.pagekite.me/models/compare_all_models/" + this.state.selectedDataset)
              .then((ires) => ires.blob())
              .then((images) => {
                  const objectURL = URL.createObjectURL(images);
                  console.log("Comparing curve URL: " + objectURL);
                  document.getElementById('compare_models_img').className -= " invisible";
                  document.getElementById('compare_models_img').src = objectURL;
      });
  }

  render() {
    console.log(this.state);
    return (
      <div>
        
        <UploadData/>

        <div className="rcorners">
          <h5>Choose a training set:</h5>
          <Select 
          options={this.state.datasetOptions}
          onChange={this.handleDropdownChange}
          >
          </Select>
        </div>

        <div className="rcorners">
          <h5>Click on a model to train:</h5>
          <h7>OBS! Neural Network and Random Forest models will take more time to train than the other models:</h7>

          <div className="d-flex bd-highlight example-parent ">

            <Row>
            {this.state.model_names_and_images.map((model, idx) => {
              return (
                <ModelCard
                  model_name={model[0]}
                  model_run_name={model[1]}
                  model_img={model[2]}
                  key={idx}
                  generatedFileName={(this.state.selectedDataset)}
                />
              );
            })}
            </Row>

          </div>
        </div>

        
        <LearningResults
          model_run_name={this.state.model_names_and_images[1]}
        />


        <div className="section_title rcorners">
            <h5 id = "compare_header" >Here you can compare all the models on the training data you have chosen: </h5>
            <h7>Note that this function will not work if the number of the points in your training data is not big enough ex less than 100.</h7>
            <br/><h7>OBS! This can take more than 15 minutes depending on the size of your training set!</h7>
            <br/><br/><Button id="compare_button" type="btn" onClick={()=>{this.compare()}}> Compare all models</Button>
            <br/><img id="compare_models_img" src="" className="invisible margin-auto information_section" alt="compare_models_img" width='100%'></img>
        </div>

        <div className="rcorners">
          <ModelUse/>
        </div>

       
      </div>
    );
  }
}

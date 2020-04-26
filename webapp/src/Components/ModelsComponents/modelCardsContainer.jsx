import React, { Component } from "react";
import ModelCard from "./modelCard";
import LearningResults from "./learningResults";
import GeneratedFilesInfo from "../SimulatorComponents/generatedfilesInfo";
import Select from 'react-select'
import ModelUse from './modelUse';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';

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
                  document.getElementById('compare_models_img').src = objectURL;
      });
  }

  render() {
    console.log(this.state);
    return (
      <div>
        <h3>Please choose a training set to train a model on, then click on a model:</h3>
        <div style={{color:"black"}}>
        <Select
        options={this.state.datasetOptions}
        onChange={this.handleDropdownChange}
        >
        </Select>
        </div>
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

        <LearningResults
          model_run_name={this.state.model_names_and_images[1]}
        />


        <div className="section_title">
            <h3 id = "compare_header" >Here you can compare all the models on the training data you have chosen: </h3>
            <h4>Note that this function will not work if the number of the points in your training data is not big enough ex less than 100.</h4>
            <h4>OBS! This can take more than 15 minutes depending on the size of your training set!</h4>
            <Button id="compare_button" type="btn" onClick={()=>{this.compare()}}> Compare all models</Button>
            <img id="compare_models_img" src="" className="visible margin-auto information_section" alt="compare_models_img"></img>
        </div>
        <ModelUse/>

       
      </div>
    );
  }
}

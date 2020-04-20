import React, { Component } from "react";
import ModelCard from "./modelCard";
import LearningResults from "./learningResults";
import GeneratedFilesInfo from "../SimulatorComponents/generatedfilesInfo";
import Select from 'react-select'


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
    fetch("http://127.0.0.1:5000/models")
      .then((res) => res.json())
      .then((data) => {
        this.setState({ model_names_and_images: data });
      })
      .catch(console.log);
      this.datasetOptions();
  }

  datasetOptions() {
        fetch("http://127.0.0.1:12345/simulator/generatedfiles")
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

  render() {
    console.log(this.state);
    return (
      <div>
        <h3>ML models:</h3>
        <div style={{color:"black"}}>
        <Select
        options={this.state.datasetOptions}
        onChange={this.handleDropdownChange}
        >
        </Select>
        </div>
        <div className="d-flex bd-highlight example-parent ">
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
        </div>
        <LearningResults
          model_run_name={this.state.model_names_and_images[1]}
        />
      </div>
    );
  }
}

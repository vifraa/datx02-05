import React, { Component } from 'react'
import ModelCard from './modelCard';
import LearningResults from './learningResults'
export default class modelCardsContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            model_names_and_images:[]
        }
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/models")
            .then(res => res.json())
            .then((data) => {
                this.setState({model_names_and_images : data});
            }).catch(console.log);
    }

    render() {
        console.log(this.state);
        return (
            <div>
                <h3>ML models:</h3>
                 <div className="d-flex bd-highlight example-parent ">
                    {this.state.model_names_and_images.map((model, idx) => {
                        return <ModelCard 
                                model_name={model[0]} 
                                model_run_name={model[1]}
                                model_img={model[2]}
                                key={idx} 
                            /> 
                    })}
                </div>
                <LearningResults model_run_name={this.state.model_names_and_images[1]}/>
            </div>
        )
    }
} 

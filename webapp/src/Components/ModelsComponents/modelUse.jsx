import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

export default class ModelUse extends Component {

    constructor(props) {
        super(props);
        this.state = {
            last_info : [],
            results: 0.0
        };
    }

   
    submitHandler = event => {
        event.preventDefault();
        event.target.className += " was-validated";
    };
    
    remove_state(){
        this.setState({ results: [] });
    }

    predict() {
        
        var data_to_predict = document.getElementById('data_to_predict').value; 

        

        fetch("http://127.0.0.1:5001/models/last_training_info")
            .then(res => res.json())
            .then((data) => {
                this.setState({ last_info: data });
                fetch("http://127.0.0.1:5001/models/predict/" + this.state.last_info[0] + "/" + this.state.last_info[1] + "/" + data_to_predict)
                .then(res => res.json())
                .then((data) => {
                    this.setState({ results: data });
                });
            }).catch(console.log);

    }

    
    render() {
        /*this.generate_individs(100,100,5)*/
        /*console.log(this.generate_individs(100,100,5));*/

        return (
            <div>

                <div className="section_title" >
                    <h3>Use The Trained Model:</h3>
                    <div id="modelUse" className="information_section" >
                    
                        <Form
                         onSubmit={this.submitHandler}
                        >
                        <Form.Row style={{display: 'block', justifyContent: 'center'}}> 
                                <Form.Control id="data_to_predict" placeholder="write the data to predict here in the following form: [0.2, .., 23]" type="text" style={{width: '90%', marginBottom: '10px'}} required/>
                        </Form.Row>
                        <Button type="submit" onClick={()=>{this.predict()}}> Predict</Button>
                        </Form>

                        <h2 id="modelUseResult">
                            {this.state.results}
                        </h2>
                    </div>


                </div>
            </div>
        )
    }
}

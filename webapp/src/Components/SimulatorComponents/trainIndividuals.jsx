import React, { Component } from 'react'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import AwesomeComponent from '../AwesomeComponent';

export default class trainIndividuals extends Component {

    constructor(props) {
        super(props);
        this.state = {
            trainings_logs: [],
            loading: true
        };
    }


    
    submitHandler = event => {
    event.preventDefault();
    event.target.className += " was-validated";
    };
    
    remove_state(){
        this.setState({ trainings_logs: [] });
    }
    
    train_population() {

        var nr_train_before = document.getElementById('nr_train_before').value; 
        var nr_train_after = document.getElementById('nr_train_after').value; 


        console.log("sending API request:")
        fetch("http://mo-yazanghafir.pagekite.me/simulator/logs/" + nr_train_before + "/" + nr_train_after)
            .then(this.state.loading = true)
            .then(res => res.json())
            .then((data) => {
                this.state.loading = false;
                this.setState({ trainings_logs: data });
                fetch("http://mo-yazanghafir.pagekite.me/simulator/individuals/pre_img")
                .then((ires) => ires.blob())
                .then((images) => {
                    const objectURL = URL.createObjectURL(images);
                    console.log("Learning curve URL: " + objectURL);
                    document.getElementById('pre_img').src = objectURL;
                    fetch("http://mo-yazanghafir.pagekite.me/simulator/individuals/post_img")
                    .then((ires) => ires.blob())
                    .then((images) => {
                        const objectURL = URL.createObjectURL(images);
                        console.log("Learning curve URL: " + objectURL);
                        document.getElementById('post_img').src = objectURL;
                });
                });
            }).catch(console.log);
    }

        
    render_individs_table(){
        var rows = this.state.trainings_logs.map(function (item, i){
            
            var entry = item.map(function (element, j) {
                return (
                     <td key={j}> {element} </td>
                );
            });
    
            return (
                <tr key={i}> {entry} </tr>
            );
    
        });
        return rows
    }

    render() {
        return (
            <div>
                <div className="section_title">
                    <h3>Train the individuals and generate logs:</h3>
                    <h4>Make sure you have generated a popuation using generator.py before running this!</h4>
                    <h4>Programs:</h4>
                    <ol>
                        <li>6w_bp_fiesta.csv</li>
                        <li>carls_power_program_BP.csv</li>
                        <li>kikuchi.csv</li>
                        <li>ogasawara_HL.csv</li>
                        <li>ogasawara_LL.csv</li>
                        <li>Random program for each individual</li>
                        <li>No pre-training program</li>
                    </ol>
                    <h5>Please enter the number of the program to train before:</h5>
                    

                    <div id="train_individuals" className="information_section">
                        

                        <Form
                         onSubmit={this.submitHandler}
                        >
                        <Form.Row style={{display: 'block', justifyContent: 'center'}}> 
                                <Form.Control id="nr_train_before" placeholder="Type the chosen program-number to train before" type="number" style={{width: '30%', marginBottom: '10px'}} required/>
                                <Form.Control id="nr_train_after" placeholder="Type the chosen program-number to train after" type="number" style={{width: '30%', marginBottom: '10px'}} required/>
                        </Form.Row>
                        <Button type="submit" onClick={()=>{this.train_population()}}> Train Individuals</Button>
                        </Form>
                        <AwesomeComponent loading={this.state.loading}/>



                        <table className="table-hover table-striped table-bordered">
                            <tbody>
                                {this.render_individs_table()}
                            </tbody>
                        </table>
                        <p className="section_notes">Here you can see the progress of one randomly chosen individual of your gym trained individuals on pre and post programs respectivly over timestamp:</p>

                        <img id="pre_img" src="" className="visible margin-auto information_section" alt="pre_img"></img>
                        <img id="post_img" src="" className="visible margin-auto information_section" alt="post_img"></img>


                    </div>
                </div>
            </div>
        )
    }
}







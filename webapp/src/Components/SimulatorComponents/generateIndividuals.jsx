import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import AwesomeComponent from '../AwesomeComponent';

export default class generateIndividuals extends Component {

    constructor(props) {
        super(props);
        this.state = {
            gen_individs: [],
            loading: true
        };
    }

   /*
    componentDidMount(){
        console.log("sending API request:")
        fetch("http://127.0.0.1:5000/simulator/individuals/5/100/5")
        .then(res => res.json())
        .then((data) => {
            this.setState({ gen_individs: data });
            console.log(data);
        }).catch(this.remove_state());
    }
    */

    submitHandler = event => {
        event.preventDefault();
        event.target.className += " was-validated";
    };
    
    remove_state(){
        this.setState({ gen_individs: [] });
    }

    generate_individs() {
        
        this.state.loading = true;
        console.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        console.log(this.state.loading);
        var n = document.getElementById('ind_n').value; 
        var bpm = document.getElementById('ind_mean').value; 
        var bpv = document.getElementById('ind_variance').value; 

        console.log("sending API request:");
        
        fetch("http://mo-yazanghafir.pagekite.me/simulator/individuals/" + n + "/" + bpm + "/" + bpv)
            .then(this.state.loading = true)
            .then(res => res.json())
            .then((data) => {
                this.state.loading = false;
                this.setState({ gen_individs: data });
                fetch("http://mo-yazanghafir.pagekite.me/simulator/individuals/img")
                .then((ires) => ires.blob())
                .then((images) => {
                    const objectURL = URL.createObjectURL(images);
                    console.log("Learning curve URL: " + objectURL);
                    document.getElementById('img_gen_individs').className -= " invisible";
                    document.getElementById('img_gen_individs').src = objectURL;
                });
            }).catch(console.log);
    }

    render_individs_table(){
        var rows = this.state.gen_individs.map(function (item, i){
            
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
        console.log("in generateIndividuals module: " );
        /*this.generate_individs(100,100,5)*/
        /*console.log(this.generate_individs(100,100,5));*/

        return (
            <div>

                <div className="section_title" >
                    <h5>Generate individuals:</h5>
                    <div id="generated_individuals" className="information_section" >
                    
                        <Form
                         onSubmit={this.submitHandler}
                        >
                        <Form.Row style={{display: 'block', justifyContent: 'center'}}> 
                                <Form.Control id="ind_n" placeholder="Number of individuals you want to generate" type="number" style={{width: '90%', marginBottom: '10px'}} required/>
                                <Form.Control id="ind_mean" placeholder="Mean of bench press max" type="number" style={{width: '90%', marginBottom: '10px'}} required/>
                            <Form.Control id="ind_variance" placeholder="Variance in bench press max" type="number" style={{width: '90%', marginBottom: '10px'}} required/>
                        </Form.Row>

                        <Button type="submit" onClick={()=>{this.generate_individs()}}> Generate Individuals</Button>
                        </Form>
                        <AwesomeComponent loading={this.state.loading}/>


                        <table className="table-hover table-striped table-bordered tablestyle">
                            <tbody>
                                {this.render_individs_table()}
                            </tbody>
                        </table>
                        
                    </div>
                        <img id="img_gen_individs" src="" className="invisible margin-auto information_section" alt="img_gen_individs" width='100%'></img>
                </div>
            </div>
        )
    }
}

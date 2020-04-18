import React, { Component } from 'react'

export default class trainIndividuals extends Component {

    constructor(props) {
        super(props);
        this.state = {
            trainings_logs: []
        };
    }

    /*
    componentDidMount(){
        console.log("sending API request:")
        fetch("http://127.0.0.1:5000/simulator/logs/1/1")
        .then(res => res.json())
        .then((data) => {
            this.setState({ trainings_logs: data });
            console.log(data);
        }).catch(this.remove_state());
    }
    */
    
    remove_state(){
        this.setState({ trainings_logs: [] });
    }
    
    train_population(nr_train_before, nr_train_after) {
        console.log("sending API request:")
        fetch("http://127.0.0.1:5000/simulator/logs/" + nr_train_before + "/" + nr_train_after)
            .then(res => res.json())
            .then((data) => {
                this.setState({ trainings_logs: data });
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
                    <div id="train_individuals" className="information_section">
                            
                        <table className="table-hover table-striped table-bordered">
                            <tbody>
                                {this.render_individs_table()}
                            </tbody>
                        </table>

                    </div>
                </div>
            </div>
        )
    }
}







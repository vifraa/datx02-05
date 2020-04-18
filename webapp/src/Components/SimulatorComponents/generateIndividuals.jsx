import React, { Component } from 'react';

export default class generateIndividuals extends Component {

    constructor(props) {
        super(props);
        this.state = {
            gen_individs: []
        };
    }

    componentDidMount(){
        console.log("sending API request:")
        fetch("http://127.0.0.1:5000/simulator/individuals/100/100/5")
        .then(res => res.json())
        .then((data) => {
            this.setState({ gen_individs: data });
            console.log(data);
        }).catch(console.log);
        console.log(this.state.gen_individs);
    }


    generate_individs(n, bpm, bpv) {
        fetch("http://127.0.0.1:5000/simulator/individuals/" + n + "/" + bpm + "/" + bpv)
            .then(res => res.json())
            .then((data) => {
                this.setState({ gen_individs: data });
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
        this.generate_individs(100,100,5)
        console.log(this.generate_individs(100,100,5));

        return (
            <div>
                <div className="section_title">
                    <h3>Generate individuals:</h3>
                    <div id="generated_individuals" className="information_section">
                    
                        <table className="table-hover table-striped table-bordered">
                            <tbody>
                                {()=>{this.render_individs_table()}}
                            </tbody>
                        </table>
                        
                    </div>


                </div>
            </div>
        )
    }
}

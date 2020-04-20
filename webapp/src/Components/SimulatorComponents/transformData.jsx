import React, { Component } from 'react'
import Select from 'react-select'
import Button from 'react-bootstrap/Button';

export default class TransformData extends Component {

     constructor(props) {
    super(props);
    this.state = {
      datasetOptions: [],
      selectedDataset: "",
      ttr_transormed: []
    };
    this.handleDropdownChange=this.handleDropdownChange.bind(this);
  }

  componentDidMount() {
      this.datasetOptions();
  }

  render_individs_table(){
        var rows = this.state.ttr_transormed.map(function (item, i){
            
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

  transorm(){

        fetch("http://127.0.0.1:5001/simulator/ttr_transform/" + this.state.selectedDataset)
            .then(res => res.json())
            .then((data) => {
                this.setState({ ttr_transormed: data });
            }).catch(console.log);
  }


    render() {
        return (
                 <div className="section_title" >
                    <h3>Transform The Generated Data to TTR format:</h3>
                    <div id="transformdata" className="information_section" >


                        <div style={{color:"black", marginBottom: '10px'}}>
                            <Select
                            options={this.state.datasetOptions}
                            onChange={this.handleDropdownChange}
                            >
                            </Select>
                        </div>

                        <Button type="submit" onClick={()=>{this.transorm()}}> Transform</Button>

                        <table className="table-hover table-striped table-bordered">
                            <tbody>
                                {this.render_individs_table()}
                            </tbody>
                        </table>
                    </div>
                </div>      
        )
    }
}

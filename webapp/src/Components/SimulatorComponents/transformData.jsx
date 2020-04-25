import React, { Component } from 'react'
import Select from 'react-select'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import AwesomeComponent from '../AwesomeComponent';

export default class TransformData extends Component {

     constructor(props) {
    super(props);
    this.state = {
      datasetOptions: [],
      selectedDataset: "",
      ttr_transormed: [],
      dataset_name:"",
      loading: true
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


    submitHandler = event => {
        event.preventDefault();
        event.target.className += " was-validated";
    };


  datasetOptions() {
        fetch("http://mo-yazanghafir.pagekite.me/simulator/generatedfiles")
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

        var ds_name = document.getElementById('dataset_name').value; 


        fetch("http://mo-yazanghafir.pagekite.me/simulator/ttr_transform/" + this.state.selectedDataset + "/" + ds_name)
            .then(this.state.loading = true)
            .then(res => res.json())
            .then((data) => {
                this.state.loading = false;
                this.setState({ ttr_transormed: data });
                fetch("http://mo-yazanghafir.pagekite.me/simulator/ttr/img/" + ds_name)
                .then((ires) => ires.blob())
                .then((images) => {
                    const objectURL = URL.createObjectURL(images);
                    console.log("Learning curve URL: " + objectURL);
                    document.getElementById('ttr_img').src = objectURL;
                });
            }).catch(console.log);
  }


    render() {
        return (
                 <div className="section_title" >
                    <h3>Transform The Generated Data to TTR format (After the Transformation You Will Find Your ready-to-train Data-set In the Models Tab):</h3>
                    <p className="section_notes">note that after the transformation you will find your ready-to-train data-set in the Models Tab:</p>
                    <p className="section_notes">now choose your generated dataset and waite for the data to be crunched!</p>

                    <div id="transformdata" className="information_section" >


                        <div style={{color:"black", marginBottom: '10px'}}>
                            <Select
                            options={this.state.datasetOptions}
                            onChange={this.handleDropdownChange}
                            >
                            </Select>


                            <Form
                                onSubmit={this.submitHandler}
                            >
                            <Form.Row style={{display: 'block', justifyContent: 'center'}}> 
                                    <Form.Control id="dataset_name" placeholder="Write the name of the transformed csv file ex. my_data_set" type="text" style={{width: '40%', marginLeft:'4px', marginTop:'10px', marginBottom: '10px'}} required/>
                            </Form.Row>
                            <Button type="submit" onClick={()=>{this.transorm()}}> Transform</Button>
                        </Form>
                            <AwesomeComponent loading={this.state.loading}/>


                        </div>


                        <table className="table-hover table-striped table-bordered">
                            <tbody>
                                {this.render_individs_table()}
                            </tbody>
                        </table>

                        <img id="ttr_img" src="" className="visible margin-auto information_section" alt="ttr_img"></img>

                    </div>
                </div>      
        )
    }
}

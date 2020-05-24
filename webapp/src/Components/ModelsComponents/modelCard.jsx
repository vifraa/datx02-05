import React, { Component } from "react";
import AwesomeComponent from '../AwesomeComponent';
import {
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBCardTitle,
  MDBIcon,
} from "mdbreact";
import Col from 'react-bootstrap/Col';
import { Link } from 'react-router-dom';
import Container from 'react-bootstrap/Container';

class modelCard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      regression_results: "",
      img_url: "",
      loading: false
    };
  }


  run_regression_and_curves(ModelName, generatedFileName) {
    fetch("http://si-yazanghafir.pagekite.me/models/regression/" + ModelName + "/" + generatedFileName)
      .then(this.state.loading = true)
      .then((res) => res.text())
      .then((data) => {
        this.setState({ regression_results: data });
        fetch("http://si-yazanghafir.pagekite.me/models/plot/" + ModelName + "/" + generatedFileName)
        .then((ires) => ires.blob())
        .then((images) => {
            this.state.loading = false;
            const objectURL = URL.createObjectURL(images);
            console.log("Learning curve URL: " + objectURL);
            this.setState({ img_url: objectURL });
            this.write_text_and_show_plot("regression_output", data, "learning_curves_output", objectURL);
        });
      })
      .catch(console.log);
  }

  write_text_and_show_plot(text_element_id, txt, img_element_id, objectURL) {
    console.log(txt);
    document.getElementById(text_element_id).innerHTML = txt;
    document.getElementById(img_element_id).src = objectURL;
    document.getElementById(img_element_id).className -= " invisible";
}


  render() {      
        
    return (
      <div> 
           <Col >
          <MDBCard
            className="mr-2 mt-3"
            cascade
            onClick={() => {
              this.run_regression_and_curves(this.props.model_run_name, this.props.generatedFileName);
            }}
          >
            <MDBCardImage
              cascade
              overlay="white-light"
              hover
              height="160px"
              width="250px"
              src={this.props.model_img}
            />
            <MDBBtn
              floating
              tag="a"
              className="ml-auto lighten-3 mdb-coalor"
              action
            >
              <MDBIcon icon="chevron-right" className="mdb-color lighten-3" />
            </MDBBtn>
            <MDBCardBody cascade>
              <MDBCardTitle id="cardTitle">
                {this.props.model_name}
              </MDBCardTitle>
              <a href={'http://mo-yazanghafir.pagekite.me/simulator/download/'+this.props.model_run_name} download={'texttest.sav'}><button className="blockBtn">Download row model</button></a>
              <a href={'http://mo-yazanghafir.pagekite.me/simulator/downloadraw/'+this.props.model_run_name} download={'texttest.sav'}><button className="blockBtn">Download wrapped model</button></a>
            </MDBCardBody>
          </MDBCard>
          <AwesomeComponent loading={this.state.loading}/>
          </Col>


        </div>
    );
  }
}

export default modelCard;

/*
<Link to="http://mo-yazanghafir.pagekite.me/simulator/download" target="_blank" download>Download after training</Link>
*/
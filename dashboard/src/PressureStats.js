import React, { Component } from 'react';
import { Chart } from "react-google-charts";
class PressureStats extends Component {
   
    render() {
        //get data from json
        return <div>  <center>     
          <p> <b>Number of Contractions</b> {this.props.num_contractions}</p>
          <p><b>Contraction per Second</b> {this.props.contraction_per_sec}</p></center>
        </div>;
    }
  }
  export default PressureStats;
import man from '../assets/images/man.png';
import github from '../assets/images/github.png'
import Resume from '../assets/images/Resume.png'
import LinkedIn from '../assets/images/LinkedIn.png'
import { useState, useEffect} from 'react';
import { faChampagneGlasses } from '@fortawesome/free-solid-svg-icons';
import Progress from './progress';
import React from 'react';

function Prfl (){

  const [persent,setPersent] = useState(10);

  const increase = () => {
    if (persent + 10 >100) return;
    setPersent(persent + 10);
  };

  const decrease = () => {
    if (persent - 10 < 0) return;
    setPersent(persent - 10);
  };

    return (
        <div className="profilestd">

            <div className="prflpic">
               <img src={man} alt="" />
               <div className="prfltexts">
                 <h1>Saidi Abdelkader</h1>
                 <h2>Senior web developer, Google</h2>
               </div>
               <ul>
                 <li><img src={Resume} alt="" /></li>
                 <li><img src={github} alt="" /></li>
                 <li><img src={LinkedIn} alt="" /></li>
               </ul>
            </div>
            <div className="profiletexts">
                <div className="propos">
                  <h1>A propos</h1>
                  <h2>Lorem ipsum dolor sit amet, consectetur adipiscing elit, <br />
                  sed do eiusmod tempor incididunt utlabore et dolore <br />
                  magna aliqua. Ut enim ad minim veniam, quis nostrud <br />
                  exercitation ullamco</h2>
                </div>

                <div className="specialite">
                  <h1>Specilaté</h1>
                  <h2>licence informatique académique</h2>
                  <h1>Université</h1>
                  <h2>USTHB</h2>
                </div>

                <div className="interesse">
                  <h1>interessé sur</h1>
                  <h2>web devlopment , inteligence <br />
                  artificiel , app devlopment, <br />
                  data analysis</h2>
                </div>
            </div>
        
            <div className="progress">
              <Progress percent={persent + '%'} />
              <div className="prgbtn">
              <button onClick={increase}>+</button> <button onClick={decrease}> - </button>
              </div>
            </div>
           
        </div>
    )
}
export default Prfl
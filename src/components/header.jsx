import students from '../assets/images/students.png';
import React from 'react';
function Header(){
    return(
        <div className="header">
            <div className='left'>

                <h1>On vous Facilite <br />
                la processus du <br />
                projet de fin d’etude </h1>

                <p>Rejoignez une communauté d'étudiants<br/> 
                et d'éducateursdédiés à la réussite des projets. </p>
            </div>
            <div className='right'>
                <img src={students} alt="" />
            </div>
        </div>
    )
}

export default Header
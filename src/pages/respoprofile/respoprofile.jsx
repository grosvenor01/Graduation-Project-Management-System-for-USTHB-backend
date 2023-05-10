import './respoprofile.css'
import RightBar from '../../components/rightbar'
import Prfl from '../../components/prfl'
import RespoCard from '../../components/respocard'
import React from 'react';
function RespoProfile (){
    return (
        <div className="respoprofile">
         <RightBar/>
         <div className="resporight">
            <Prfl/>
            <h1>Themes a valider</h1>
            <div className="repocards">
                <RespoCard/>
                <RespoCard/>
                <RespoCard/>
                <RespoCard/>
            </div>
         </div>
        </div>
    )
}

export default RespoProfile
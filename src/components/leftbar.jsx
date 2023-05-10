import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass, faEnvelope, faPaperPlane, faBell} from '@fortawesome/free-solid-svg-icons'
import UserName from './username'
import NotificationsBar from './notificationsbar'
import { useState } from 'react'
import React from 'react';

function LeftBar(){

    const [openModal, setOpenModal] = useState(false)   

    return (
        <div>
        <div className="leftbar">

            <div className="hsearch">
               <div className="searchbar">
                   <FontAwesomeIcon icon={faMagnifyingGlass} className='serachicon'/>
                   <input className='linput' type="text" placeholder='Search' />
               </div>
               <div className="notificon">
                   <FontAwesomeIcon icon={faBell} className='bell' onClick={()=>setOpenModal(true)} />
                   <NotificationsBar open={openModal} onClose={()=>setOpenModal(false)} />
               </div>
               <div className="send">
                   <FontAwesomeIcon icon={faEnvelope} className='briya'/>
               </div>
            </div>

            <div className="lefttexts">
                <h1>Suggestion Pour vous</h1>
                <h2>All</h2>
            </div>

            <div className="user">
                <UserName/>
                <UserName/>
                <UserName/>
                <UserName/>
            </div>
        </div>
        </div>
    )
}

export default LeftBar
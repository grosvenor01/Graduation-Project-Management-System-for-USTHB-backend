import profilepic from '../assets/images/profilepic.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {
    faThumbsUp, faComment, faCheckDouble, faCheck,
    faClockRotateLeft, faEllipsisVertical
} from '@fortawesome/free-solid-svg-icons'
import Comment from './comment';
import { useState } from 'react';
import { useEffect } from 'react';
import React from 'react';

function Question() {

    const [comment, setComment] = useState("")
    const [isLoading,setIsLoading]=useState(false)
    const [comments, setComments] = useState([])
    const onChangeHandler = (e) => {
        setComment(e.target.value)
    }
    const onClickHandler = (e) => {
        setComments((comments) => [...comments, comment])
    }

    const [posts, setPosts] = useState([]);
    useEffect(() => {
        fetch('http://localhost:8000/api/recommander/', {
            credentials: 'include'
          })
            .then(response => response.json())
            .then(data => setPosts(data));
    }, []);
    const onClickReturn = (postId, user) => {
        setIsLoading(true);
        const data = { postId, user };
        fetch(`http://localhost:8000/api/postuler/${data.postId}`, {
          method: 'POST',
          credentials: 'include',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        })
          .then(response => response.json())
          .then(data => {
            setIsLoading(false);
          })
          .catch(error => {
            console.error('Error:', error);
            setIsLoading(false);
          });
      };
    return (
        <div>
            {posts.map((post, index) => (
                
                <div className="question">
                    <div className="qstprofil">
                        <img src={profilepic} alt="" />
                        {posts.length > 0 && (
                         <div className="qsttexts">
                            <h1 key={posts[index].id}>{posts[index].user["username"]}</h1>
                            <h2><FontAwesomeIcon icon={faClockRotateLeft} />   Il y’a 3min</h2>
                        </div>
                        )}
                        <div className="points">
                            <button className='pointsicon' onClick={()=>onClickReturn(post.id,post.user.id)} disabled={isLoading}>Postuler</button>
                        </div>
                    </div>
                    {posts.length > 0 && (
                        <div className='jsshow'>
                            <h1>{posts[index].main_text}</h1>
                            <h3 className='sqtpara'> {posts[index].description_text}</h3>
                            <div className="tags">
                                {posts[index].keywords.split(",").map((keyword, index) => (
                                    <h4 key={index}>{keyword}</h4>
                                ))}
                            </div>
                        </div>
                    )}


                    <hr />

                    <ul className='qstlist'>
                        <li><FontAwesomeIcon icon={faThumbsUp} />     like</li>
                        <li className='listt'><FontAwesomeIcon icon={faComment} />     Comment</li>
                        <li className='listt'><FontAwesomeIcon icon={faCheckDouble} />     vu par 1k</li>
                    </ul>
                    {comments.map((text) => (
                        <div>
                            <div className='qstcomment'>
                                <img src={profilepic} alt="" />
                                <div className="qstinput">
                                    <h1>Full name</h1>
                                    <div className="your-comment">{text}</div>
                                </div>
                            </div>
                            <hr />
                        </div>
                    ))}

                    <div className="qstcomment">
                        <img src={profilepic} alt="" />
                        <div className="qstinput">
                            <h1>Full name</h1>
                            <input type="text"
                                className='commentinput'
                                placeholder='ajouter votre commentaire ...'
                                value={comment}
                                onChange={onChangeHandler}
                            />
                        </div>
                        <div className="check">
                            <FontAwesomeIcon
                                icon={faCheck}
                                className='checkicon'
                                onClick={onClickHandler}
                            />
                        </div>
                    </div>

                </div>
            ))}
        </div>
    )
}

export default Question
import React, { useState } from 'react'
import "./System.css"
import { useMutation, useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Pagination } from '@mui/material'
export default function System() {

  const [pages, setPages] = useState(1)

  const {data} =  useQuery({
    queryKey: ["data"],
    queryFn: async() => {
        const res = await axios.get("https://run.mocky.io/v3/1e0d344b-8888-446a-9e4c-99cce98e917e")
        return res.data
    },
    refetchInterval: 1000
  })

  

  const changePage = (e, page) => {
    setPages(page)
  }


  return (
    <div className="system__cover">
      <h2 className="system__title">Система - Результат проверки в реальном времени</h2>
      <ul className="system__result-menu">
        {
          data
          ?.filter(item => item.id === pages)
          ?.map(pref => {
            return(
             <>
                <li>
                  <h4>source_ip:</h4>
                  <p>{pref?.source_ip}</p>
                </li>
                <li>
                  <h4>destination_ip:</h4>
                  <p>{pref?.destination_ip}</p>
                </li>
                <li>
                  <h4>protocol:</h4>
                  <p>{pref?.protocol}</p>
                </li>
                <li>
                  <h4>source_port:</h4>
                  <p>{pref?.source_port}</p>
                </li>
                <li>
                  <h4>destination_port:</h4>
                  <p>{pref?.destination_port}</p>
                </li>
                <li>
                  <h4>packet_length:</h4>
                  <p>{pref?.packet_length}</p>
                </li>
                <li>
                  <h4>flags:</h4>
                  <p>{pref?.flags}</p>
                </li>
                <li>
                  <h4>threat:</h4>
                  <p>{pref?.threat}</p>
                </li>
                <li>
                  <h4>is_danger:</h4>
                  <p style={{color: pref?.is_danger && 'red'}}>{pref?.is_danger}</p>
                </li>
             </>
            )
          })
        }
      </ul>
      <div className="system__controllers">
      <Pagination page={pages} onChange={changePage} count={data?.length} variant="outlined" shape="rounded" />
      </div>
    </div>
  )
}

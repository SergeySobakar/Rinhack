import React from 'react'
import "./Aside.css"
import { NavLink } from 'react-router-dom'
import shieldIcon from "../../assets/shield.svg"
import systemIcon from "../../assets/system.svg"
import mailingIcon from "../../assets/mailing.svg"
import faqIcon from "../../assets/faq.svg"

export default function Aside() {
  return (
    <aside className="sideBarCover">
        <div className="sideBarInner">
            <div>
              <h1 className="title">
                <img src={shieldIcon} alt="" />
                <p>NeurealShield</p>
              </h1>
              <div className="menu">
                <NavLink
                  to={"/"}
                  className={({ isActive}) =>
                  isActive ? "link__item active" : "link__item"
                }
                >
                  <img src={systemIcon} alt="" />
                  <p>Система</p>
                </NavLink>
                <NavLink
                  to={"/newsletter"}
                  className={({ isActive}) =>
                  isActive ? "link__item active" : "link__item"
                }
                >
                  <img src={mailingIcon} alt="" />
                  <p>Рассылка</p>
                </NavLink>
              </div>
            </div>
            <NavLink
                to={"/faq"}
                className={({ isActive}) =>
                isActive ? "faq link__item active" : "faq link__item"
              }
              >
                <img src={faqIcon} alt="" />
                <p>FAQ</p>
              </NavLink>
        </div>
    </aside>
  )
}

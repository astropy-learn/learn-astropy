import React from 'react';
import { Link } from 'gatsby';
import styled from 'styled-components';

import numfocusStamp from '../../static/Numfocus_stamp.png';
import dunlapLogo from '../../static/dunlap-logo.png';

const FullWidthContainer = styled.div`
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin: var(--astropy-size-xl) -50vw 0;
  background-color: rgb(250, 250, 250);
`;

const StyledFooter = styled.footer`
  margin: 0 auto;
  max-width: var(--astropy-content-width);
  padding: var(--astropy-size-m) var(--astropy-size-s);

  h2 {
    font-size: var(--astropy-font-size-ml);
    font-weight: 400;
  }

  nav ul {
    list-style: none;
    padding-left: 0;
  }

  nav a {
    font-weight: 500;
  }

  nav ul li:first-child a {
    font-weight: 700;
  }

  .footer-content-layer {
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: flex-start;
    margin: var(--astropy-size-m) 0;
  }

  .sponsors,
  .code-of-conduct {
    width: 24rem;
  }

  .code-of-conduct p {
    margin-bottom: 0;
  }

  .numfocusStamp {
    margin-top: var(--astropy-size-l);
  }

  .sponsors .numfocusStamp__image {
    width: 16rem;
  }

  .sponsors .dunlapLogo__image {
    margin-top: var(--astropy-size-m);
    width: 20rem;
  }

  .copyright {
    margin-top: var(--astropy-size-xl);
  }
`;

/*
 * Footer component (contained within a Layout component).
 */
export default function Footer() {
  return (
    <FullWidthContainer>
      <StyledFooter>
        <nav>
          <ul>
            <li>
              <Link to="/contributing/">Contribute to Learn Astropy</Link>
            </li>
          </ul>
        </nav>
        <div className="footer-content-layer">
          <article className="code-of-conduct">
            <h2>Code of Conduct</h2>
            <p>
              The Astropy project is committed to fostering an inclusive
              community. The community of participants in open source Astronomy
              projects is made up of members from around the globe with a
              diverse set of skills, personalities, and experiences. It is
              through these differences that our community experiences success
              and continued growth.{' '}
              <a href="https://www.astropy.org/code_of_conduct.html">
                Learn more.
              </a>
            </p>
          </article>
          <article className="sponsors">
            <h2>Sponsors</h2>
            <a href="http://www.dunlap.utoronto.ca">
              <img className="dunlapLogo__image" src={dunlapLogo} alt="" />
            </a>
            <p>
              The Learn Astropy website was developed under a grant by the{' '}
              <a href="http://www.dunlap.utoronto.ca">
                University of Toronto Dunlap Institute for Astrophysics.
              </a>{' '}
            </p>
            <div className="numfocusStamp">
              <a href="https://numfocus.org">
                <img
                  className="numfocusStamp__image"
                  src={numfocusStamp}
                  alt="A fiscally sponsored project of NumFOCUS"
                />
              </a>
            </div>
          </article>
        </div>
        <p className="copyright">
          Copyright {new Date().getFullYear()} The Astropy Developers
        </p>
      </StyledFooter>
    </FullWidthContainer>
  );
}

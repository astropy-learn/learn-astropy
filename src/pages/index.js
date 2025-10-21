import React from 'react';
import PropTypes from 'prop-types';

import { InstantSearch, Configure } from 'react-instantsearch-dom';

import Layout from '../components/layout';
import {
  SearchLayout,
  SearchRefinementsSection,
} from '../components/searchLayout';
import SEO from '../components/seo';
import PageCover from '../components/pageCover';
import searchClient from '../searchClient';
import { StyledHits } from '../components/instantsearch/hits';
import RefinementList from '../components/instantsearch/refinementList';
import SearchBox from '../components/instantsearch/searchBox';
import PrioritySort from '../components/instantsearch/virtualPrioritySort';
import ResultCard from '../components/resultCard';

export default function IndexPage({ location }) {
  return (
    <Layout>
      <SEO location={location} title="Home" />
      <PageCover>
        <h1>Learn Astropy</h1>
        <p>
          Learn how to use Python for research in astronomy with tutorials and
          guides covering Astropy and the broader astronomy Python ecosystem.
        </p>
      </PageCover>

      <InstantSearch searchClient={searchClient} indexName="prod_learn_astropy">
        <Configure distinct facetingAfterDistinct />
        <PrioritySort
          priorityRefinement="prod_learn_astropy_priority"
          relevanceRefinement="prod_learn_astropy"
        />
        <SearchLayout>
          <div className="search-box-area">
            <SearchBox />
          </div>
          <div className="search-refinements-area">
            <SearchRefinementsSection>
              <h2>Format</h2>
              <RefinementList attribute="content_type" />
            </SearchRefinementsSection>
            <SearchRefinementsSection>
              <h2>Astropy packages</h2>
              <RefinementList
                attribute="astropy_package_keywords"
                limit={15}
                showMore
                showMoreLimit={30}
                searchable
              />
            </SearchRefinementsSection>
            <SearchRefinementsSection>
              <h2>Python packages</h2>
              <RefinementList
                attribute="python_package_keywords"
                limit={15}
                showMore
                showMoreLimit={30}
                searchable
              />
            </SearchRefinementsSection>
            <SearchRefinementsSection>
              <h2>Tasks</h2>
              <RefinementList
                attribute="task_keywords"
                limit={15}
                showMore
                showMoreLimit={30}
                searchable
              />
            </SearchRefinementsSection>
            <SearchRefinementsSection>
              <h2>Science domains</h2>
              <RefinementList
                attribute="science_keywords"
                limit={15}
                showMore
                showMoreLimit={30}
                searchable
              />
            </SearchRefinementsSection>
          </div>
          <div className="search-results-area">
            <StyledHits hitComponent={ResultCard} />
          </div>
        </SearchLayout>
      </InstantSearch>
    </Layout>
  );
}

IndexPage.propTypes = {
  location: PropTypes.shape({
    pathname: PropTypes.string.isRequired,
  }),
};

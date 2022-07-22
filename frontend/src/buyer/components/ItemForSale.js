import React from "react";
import XX99 from "../../assets/product-xx99-mark-two-headphones/desktop/image-category-page-preview.jpg";
import {
  StyledWholeItem,
  StyledDescriptionBox,
  StyledInnerDescriptionBox,
} from "../styles/ItemForSale";
import { StyledSeeProduct } from "../styles/SeeProductButton";

const ItemForSale = ({ image, name, description, idx }) => {
  return (
    <StyledWholeItem layout={idx % 2 !== 0 && "row-reverse"}>
      <img src={image} alt="Headphones" />
      <StyledDescriptionBox>
        <StyledInnerDescriptionBox>
          <h5>NEW PRODUCT</h5>
          <h2>{name}</h2>
          <p>{description}</p>
          <StyledSeeProduct>SEE PRODUCT</StyledSeeProduct>
        </StyledInnerDescriptionBox>
      </StyledDescriptionBox>
    </StyledWholeItem>
  );
};

export default ItemForSale;

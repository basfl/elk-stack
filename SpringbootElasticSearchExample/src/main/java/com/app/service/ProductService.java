package com.app.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.app.entity.Product;
import com.app.repo.ProductRepo;

import java.util.List;

@Service
public class ProductService {

    @Autowired
    private ProductRepo  productRepo;

    public Iterable<Product> getProducts() {
     return productRepo.findAll();
    }

    public Product insertProduct(Product product) {
        return productRepo.save(product);
    }

    public Product updateProduct(Product product, int id) {
        Product product1  = productRepo.findById(id).get();
//        product1.setPrice(product.getPrice());
//        return product1;
        return null;
    }

    public void deleteProduct(int id ) {
        productRepo.deleteById(id);
    }
}
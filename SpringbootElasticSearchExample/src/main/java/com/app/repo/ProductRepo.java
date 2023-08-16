package com.app.repo;


import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import com.app.entity.Product;

public interface ProductRepo extends ElasticsearchRepository<Product,Integer> {

        }

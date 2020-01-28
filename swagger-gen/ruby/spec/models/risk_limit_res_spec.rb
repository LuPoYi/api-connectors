=begin
#Bybit API

### REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]  

OpenAPI spec version: 1.0.0
Contact: support@bybit.com
Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.8

=end

require 'spec_helper'
require 'json'
require 'date'

# Unit tests for SwaggerClient::RiskLimitRes
# Automatically generated by swagger-codegen (github.com/swagger-api/swagger-codegen)
# Please update as you see appropriate
describe 'RiskLimitRes' do
  before do
    # run before each test
    @instance = SwaggerClient::RiskLimitRes.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of RiskLimitRes' do
    it 'should create an instance of RiskLimitRes' do
      expect(@instance).to be_instance_of(SwaggerClient::RiskLimitRes)
    end
  end
  describe 'test attribute "position"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  describe 'test attribute "risk"' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end

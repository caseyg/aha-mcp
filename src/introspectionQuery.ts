export const introspectionQuery = `
  query IntrospectionQuery {
    __schema {
      queryType { name }
      mutationType { name }
      subscriptionType { name }
      types {
        ...FullType
      }
      directives {
        name
        description
        locations
        args {
          ...InputValue
        }
      }
    }
  }

  fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
      name
      description
      args {
        ...InputValue
      }
      type {
        ...TypeRef
      }
      isDeprecated
      deprecationReason
    }
    inputFields {
      ...InputValue
    }
    interfaces {
      ...TypeRef
    }
    enumValues(includeDeprecated: true) {
      name
      description
      isDeprecated
      deprecationReason
    }
    possibleTypes {
      ...TypeRef
    }
  }

  fragment InputValue on __InputValue {
    name
    description
    type { ...TypeRef }
    defaultValue
  }

  fragment TypeRef on __Type {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
        ofType {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                }
              }
            }
          }
        }
      }
    }
  }
`;

export const simpleIntrospectionQuery = `
  query {
    __schema {
      types {
        name
        kind
      }
    }
  }
`;

export const listTypesQuery = `
  query {
    __schema {
      types {
        name
        kind
      }
    }
  }
`;

export const queryTypeIntrospectionQuery = `
  query {
    __schema {
      queryType {
        fields {
          name
          description
          args {
            name
            type {
              name
              kind
            }
          }
        }
      }
    }
  }
`;

export const mutationTypeIntrospectionQuery = `
  query {
    __schema {
      mutationType {
        fields {
          name
          description
          args {
            name
            type {
              name
              kind
            }
          }
        }
      }
    }
  }
`;

export const typeIntrospectionQuery = (typeName: string) => `
  query TypeIntrospection {
    __type(name: "${typeName}") {
      name
      kind
      description
      fields {
        name
        description
        type {
          kind
          name
          ofType {
            kind
            name
          }
        }
      }
    }
  }
`;

export const searchQueriesIntrospectionQuery = (searchTerm: string) => `
  query SearchQueries {
    __schema {
      queryType {
        fields {
          name
          description
          args {
            name
            description
            type {
              ...TypeRef
            }
            defaultValue
          }
          type {
            ...TypeRef
          }
        }
      }
    }
  }
  
  fragment TypeRef on __Type {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
      }
    }
  }
`;

export const searchMutationsIntrospectionQuery = (searchTerm: string) => `
  query SearchMutations {
    __schema {
      mutationType {
        fields {
          name
          description
          args {
            name
            description
            type {
              ...TypeRef
            }
            defaultValue
          }
          type {
            ...TypeRef
          }
        }
      }
    }
  }
  
  fragment TypeRef on __Type {
    kind
    name
    ofType {
      kind
      name
      ofType {
        kind
        name
      }
    }
  }
`;
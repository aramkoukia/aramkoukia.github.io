---
layout: post
title: "Azure DocumentDB vs SQL Azure, a performance comparison"
date: 2016-12-09
description: "UPDATE:"
image: /assets/img/2016-12-09-azure-documentdb-vs-sql-azure-a-performance-comparison/1.jpg
medium_url: https://medium.com/@aramkoukia/azure-documentdb-vs-sql-azure-a-performance-comparison-da5feec95b72
---

### Azure DocumentDB vs SQL Azure, a performance comparison

![](/assets/img/2016-12-09-azure-documentdb-vs-sql-azure-a-performance-comparison/1.jpg)

### UPDATE:

*“Please see* [*this other post*](https://koukia.ca/azure-documentdb-vs-sql-azure-performance-comparison-revised-178a90038146#.25sh5gsf6) *about the correct numbers after fixing some issues in the code:”*

<https://koukia.ca/azure-documentdb-vs-sql-azure-performance-comparison-revised-178a90038146#.25sh5gsf6>

In [this post](https://koukia.ca/microsoft-and-nosql-data-store-for-your-modern-cloud-application-e57885b18a5f#.u8l5xlmv8) a while a go I introduced the Azure DocumentDB and showed you how you can connect to it, create documents there and read documents with queries.

In terms of SQL Azure there is nothing special involved and it works exactly how on-premise SQL Server works, and you can use ADO.NET, Entity Framework or any other technique that you might want to use for SQL Azure.

Now I want to do a performance comparison on these two data stores and see which one will do better!

So, I’m just going to add a class to the solution I created for the DocumentDB that will connect to SQL Azure and insert some data and reads some data from it. I’ll skip the steps on how to create SQL Azure Database and tables in it as there is nothing really special about that you could do it using normal TSQL commands that you already are familiar with.

For SQL Azure section, I created the database in Azure and then used an Entity Framework model to interact with the database, so here the class for dealing with SQL Azure:

```
public class SQLAzureProvider {     public void AddCandidate(Candidate candidate)     {         var dbcontext = new SQLAzureDemo.AramPerformanceTestDBEntities();
```

```
dbcontext.Candidates.Add(candidate);
```

```
dbcontext.SaveChanges();     }         public long GetLastCandidateId()     {          var dbcontext = new SQLAzureDemo.AramPerformanceTestDBEntities();          return dbcontext.Candidates.Max(m=>m.CandidateId);     }
```

```
public List<Candidate> GetCandidateById(int candidateId)     {          var dbcontext = new SQLAzureDemo.AramPerformanceTestDBEntities();                   return dbcontext.Candidates.Where(m=>m.CandidateId == candidateId).ToList();     }
```

```
public List<Candidate> GetCandidatesByName(string candidateName)       {            var dbcontext = new SQLAzureDemo.AramPerformanceTestDBEntities();
```

```
return dbcontext.Candidates.Where(m => m.FirstName == candidateName).Take(50).ToList();     }
```

```
public List<Candidate> GetCandidatesList(int pageSize)     {         var dbcontext = new SQLAzureDemo.AramPerformanceTestDBEntities();         return dbcontext.Candidates.Take(pageSize).ToList();     } }
```

And here the same old class from previous post to talk to DocumentDb but with some additional data to be able to do the performance tests:

```
public class DocumentDBProvider {     private static string EndpointUrl = "https://YourDocumentDbName.documents.azure.com:443/";     private static string AuthorizationKey = "Take this code from your Azure Management Portal";
```

```
private static string DatabaseName = "InterviewDB";
```

```
private static string DocumentCollectionName = "InterviewCollection";     public async Task<DocumentCollection> CreateDatabaseAndDocumentCollection()   {       var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);
```

```
Database database = await client.CreateDatabaseAsync(new Database { Id = DatabaseName });
```

```
DocumentCollection documentCollection = await client.CreateDocumentCollectionAsync(database.CollectionsLink, new DocumentCollection { Id = DocumentCollectionName } );        return documentCollection;   }
```

```
public string GetDocumentLink() {     var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);
```

```
Database database = client.CreateDatabaseQuery().Where(db => db.Id == DatabaseName).AsEnumerable().FirstOrDefault();
```

```
DocumentCollection documentCollection = client.CreateDocumentCollectionQuery(database.CollectionsLink).Where(db => db.Id == DocumentCollectionName).AsEnumerable().FirstOrDefault();
```

```
return documentCollection.DocumentsLink; }
```

```
public DocumentClient GetClient() {    return new DocumentClient(new Uri(EndpointUrl), AuthorizationKey); }
```

```
public async Task<ResourceResponse<Document>> AddCanidateToCollection(string documentLink,DocumentClient client, Candidate candidate) {   return await client.CreateDocumentAsync(documentLink, candidate); }
```

```
public List<Candidate> GetCandidatesCollection() {   var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);   Database database = client.CreateDatabaseQuery().Where(db => db.Id == DatabaseName).AsEnumerable().FirstOrDefault();      DocumentCollection documentCollection = client.CreateDocumentCollectionQuery(database.CollectionsLink).Where(db => db.Id == DocumentCollectionName).AsEnumerable().FirstOrDefault();
```

```
return client.CreateDocumentQuery<Candidate>(documentCollection.DocumentsLink).ToList();
```

```
}
```

```
public List<Candidate> GetCandidateById(int candidateId) {    var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);
```

```
Database database = client.CreateDatabaseQuery().Where(db => db.Id == DatabaseName).AsEnumerable().FirstOrDefault();     DocumentCollection documentCollection = client.CreateDocumentCollectionQuery(database.CollectionsLink).Where(db => db.Id == DocumentCollectionName).AsEnumerable().FirstOrDefault();
```

```
return client.CreateDocumentQuery<Candidate>(documentCollection.DocumentsLink).Where(m => m.CandidateId == candidateId).Select(m => m).ToList();   }
```

```
public List<Candidate> GetCandidatesByName(string candidateName)   {      var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);
```

```
Database database = client.CreateDatabaseQuery().Where(db => db.Id == DatabaseName).AsEnumerable().FirstOrDefault();             DocumentCollection documentCollection = client.CreateDocumentCollectionQuery(database.CollectionsLink).Where(db => db.Id == DocumentCollectionName).AsEnumerable().FirstOrDefault();
```

```
return client.CreateDocumentQuery<Candidate>(documentCollection.DocumentsLink).Where(m => m.CandidateFirstName == candidateName).Take(50).Select(m => m).ToList();   }
```

```
public List<Candidate> GetCandidatesList(int pageSize) {     var client = new DocumentClient(new Uri(EndpointUrl), AuthorizationKey);     Database database = client.CreateDatabaseQuery().Where(db => db.Id == DatabaseName).AsEnumerable().FirstOrDefault();
```

```
DocumentCollection documentCollection = client.CreateDocumentCollectionQuery(database.CollectionsLink).Where(db => db.Id == DocumentCollectionName).AsEnumerable().FirstOrDefault();
```

```
return client.CreateDocumentQuery<Candidate>(documentCollection.DocumentsLink).Take(pageSize).ToList(); } }
```

Here is the sample test method for inserting data into SQL Azure:

```
[TestMethod] public void Add10CandidatesToSQLAzure() {   Stopwatch stopWatch = new Stopwatch();   var sut = new SQLAzureDemo.SQLAzureProvider();   var maxId = sut.GetLastCandidateId() + 1;   stopWatch.Start();   for (int i = 0; i < 10; i++)   {      var candidate = new SQLAzureDemo.Candidate()      {         FirstName = "Aram",         LastName = "Koukia",         CandidateId = maxId + i, CandidateStatusId = 1      };      sut.AddCandidate(candidate); } stopWatch.Stop();           Trace.WriteLine("Add 10 rows to SQL Azure took:" +   stopWatch.Elapsed);      Trace.Flush(); }
```

And the test method to insert data into DocumentDB:

```
[TestMethod] public async Task Add10CandidatesToDocumentDB() {    var sut = new DocumentDBDemo.DocumentDBProvider();    Stopwatch stopWatch = new Stopwatch();    var documentLink = sut.GetDocumentLink();    var documentClient = sut.GetClient();    stopWatch.Start();    for (int i = 0; i < 10; i++)    {       var candidate = new Candidate()       {          CandidateFirstName = "Aram",          CandidateLastName = "Koukia",          CandidateId = 1,          Status = new CandidateStatus()         { CandidateStatusId = 1, CandidateStatusName = "New" }       };       await sut.AddCanidateToCollection(documentLink, documentClient, candidate);    }    stopWatch.Stop();    Trace.WriteLine("Add 10 rows to DocumentDB took:" + stopWatch.Elapsed);    Trace.Flush(); }
```

All I did for the other test methods was to change the for loop range above to be 100,1000 and 10000 for both cases and log the elapsed time with a StopWatch.

These are the test cases that I considered to do the comparisons:

1. Call both data stores to insert 10 entities
2. Call both data stores to insert 100 entities
3. Call both data stores to insert 1000 entities
4. Call both data stores to insert 10,000 entities
5. Read some rows from both data stores, with similar conditions (same result set) — queried both stores with CandidateName = “Aram” condition and took 50 rows of the result
6. Read both data stores with one specific CandidateId
7. Read 1000 rows with no condition from both stores.

Now the moment of truth (I remember a friend of mine used to say that the truth can only be found in the code!)

“Insert” performance comparison table:

SQL Azure(s) DocumentDB(s)

Insert 10 rows 2.8106547 1.3581273

Insert 100 rows21.9046744 9.0996640

Insert 1,000 rows 123.4606796 81.5708659

Insert 10,000 rows 2129.6755560 871.5634444

“Read” performance comparison table:

SQL Azure(s) DocumentDB(s) Query with CandidateId

0.0744431 1.0356455

Query 1000 rows no condition

0.2373464 1.0654554

Query with CandidateName and return 50 rows

0.78361871 .0721330

And the winner is…..

### UPDATE:

*“Please see* [*this other post*](https://koukia.ca/azure-documentdb-vs-sql-azure-performance-comparison-revised-178a90038146#.25sh5gsf6) *about the correct numbers after fixing some issues in the code:”*

<https://koukia.ca/azure-documentdb-vs-sql-azure-performance-comparison-revised-178a90038146#.25sh5gsf6>

Well looks like for the data that I used, about (20,000 rows and documents) with the same values in all columns, DocumentDB goes into problems accessing them, even with limited FeedOptions (set to 1 or 5 or 1000) it takes a long time to query!

But in case of insert operation looks like DocumentDb works way better, and it is probably because of the fact that there is no constraint of any kind there to limit the insert operation.

I’ll try to check the same comparison with some more test data and see what comes out of it…

You can find the code for this test on Github here: <https://github.com/aramkoukia/DocumentDbvsSQLAzure>
